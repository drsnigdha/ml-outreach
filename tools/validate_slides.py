import sys
from html.parser import HTMLParser
import os

class SlideValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag_stack = []
        self.slide_count = 0
        self.errors = []
        self.nested_slide_detected = False
        # HTML5 self-closing tags that do not require closing tags
        self.self_closing = {'img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'col', 'embed', 'param', 'area', 'track', 'wbr', 'base'}

    def handle_starttag(self, tag, attrs):
        tag_lower = tag.lower()
        if tag_lower in self.self_closing:
            return  # Skip self-closing tags
            
        # Track classes to identify slide containers
        attrs_dict = dict(attrs)
        class_attr = attrs_dict.get('class', '')
        classes = class_attr.split()
        
        # Recognize various slide container elements and classes (both div and section)
        is_slide = (tag_lower in ('div', 'section') and any(c in ('slide', 'slide-transition', 'slide-container', 'slide-fade') for c in classes))
        
        if is_slide:
            # Level 2 Check: Verify no slide is nested inside another slide
            for parent_tag, parent_is_slide, line, col in self.tag_stack:
                if parent_is_slide:
                    self.errors.append(
                        f"  ❌ NESTING ERROR: Slide container opened at line {self.getpos()[0]}, col {self.getpos()[1]} "
                        f"is nested inside another slide container (opened at line {line}, col {col})"
                    )
                    self.nested_slide_detected = True
            
            self.slide_count += 1
            
        self.tag_stack.append((tag_lower, is_slide, self.getpos()[0], self.getpos()[1]))

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower in self.self_closing:
            return  # Skip self-closing tags
            
        if not self.tag_stack:
            self.errors.append(f"  ❌ BALANCE ERROR: Extra closing tag '</{tag}>' at line {self.getpos()[0]}, col {self.getpos()[1]}")
            return
            
        open_tag, is_slide, line, col = self.tag_stack.pop()
        if open_tag != tag_lower:
            self.errors.append(
                f"  ❌ BALANCE ERROR: Closed '</{tag}>' at line {self.getpos()[0]}, col {self.getpos()[1]} "
                f"but expected '</{open_tag}>' (opened at line {line}, col {col})"
            )
            # Try to recover by pushing the expected tag back on
            self.tag_stack.append((open_tag, is_slide, line, col))

def validate_presentation(file_path, expected_slides=36):
    file_name = os.path.basename(file_path)
    print(f"Parsing HTML structure of {file_name}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
        
    validator = SlideValidator()
    validator.feed(html_content)
    
    # Check for unclosed tags at the end of file
    if validator.tag_stack:
        for tag, is_slide, line, col in reversed(validator.tag_stack):
            validator.errors.append(f"  ❌ BALANCE ERROR: Unclosed tag '<{tag}>' opened at line {line}, col {col}")
            
    # Report errors
    if validator.errors:
        print(f"Status: ❌ FAILED ({len(validator.errors)} structural errors found in {file_name})")
        for error in validator.errors:
            print(error)
        sys.exit(1)
    
    # Level 3 Check: Verify exact slide count
    if validator.slide_count != expected_slides:
        print(f"Status: ❌ FAILED (Slide count mismatch in {file_name})")
        print(f"  ❌ COUNT ERROR: Expected exactly {expected_slides} slides, but found {validator.slide_count}!")
        sys.exit(1)
        
    print(f"✅ SUCCESS: All {validator.slide_count} slides in {file_name} are perfectly balanced, flat, and non-nested!\n")
    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 validate_slides.py <path_to_html_file> [expected_slides]")
        sys.exit(1)
        
    target_file = sys.argv[1]
    slides = int(sys.argv[2]) if len(sys.argv) > 2 else 36
    validate_presentation(target_file, slides)
