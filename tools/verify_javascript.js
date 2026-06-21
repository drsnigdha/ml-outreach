const fs = require('fs');
const path = require('path');
const vm = require('vm');

function validateHtmlScripts(filePath) {
    console.log(`Extracting and compiling JavaScript from ${filePath}...`);
    let htmlContent;
    try {
        htmlContent = fs.readFileSync(filePath, 'utf8');
    } catch (err) {
        console.error(`Error reading file: ${err.message}`);
        process.exit(1);
    }

    // Regex to extract inline script blocks (ignoring external scripts with 'src')
    const scriptRegex = /<script\b[^>]*>([\s\S]*?)<\/script>/gi;
    let match;
    let blockIndex = 1;
    let hasErrors = false;

    while ((match = scriptRegex.exec(htmlContent)) !== null) {
        const scriptTag = match[0];
        const scriptContent = match[1].trim();

        // Skip external script tags
        if (/<script\b[^>]*\bsrc\s*=/i.test(scriptTag)) {
            continue;
        }

        // Skip empty script tags
        if (scriptContent.length === 0) {
            continue;
        }

        try {
            // Compile script in virtual machine context to catch syntax errors
            new vm.Script(scriptContent, { filename: `${path.basename(filePath)} -> script_block_${blockIndex}.js` });
            console.log(`  ✅ Script block #${blockIndex} compiles successfully!`);
        } catch (err) {
            console.error(`  ❌ SYNTAX ERROR in script block #${blockIndex}:`);
            console.error(err.stack.split('\n').slice(0, 5).join('\n')); // Show the main error lines
            hasErrors = true;
        }
        blockIndex++;
    }

    if (hasErrors) {
        process.exit(1);
    }
    console.log(`✅ SUCCESS: All JavaScript in ${path.basename(filePath)} is syntactically sound!\n`);
}

if (process.argv.length < 3) {
    console.log("Usage: node verify_javascript.js <path_to_html_file>");
    process.exit(1);
}

const targetFile = process.argv[2];
validateHtmlScripts(targetFile);
