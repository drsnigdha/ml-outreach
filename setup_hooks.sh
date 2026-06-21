#!/bin/bash

# --- Color Codes for UI ---
GREEN='\033[0;32m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "\n${BOLD}${BLUE}=== ⚙️  Hardening Your Repository: Setting Up Git Hooks  === ${NC}\n"

# 1. Make the pre-commit script executable
chmod +x .githooks/pre-commit
echo -e "  ✅ Made .githooks/pre-commit executable."

# 2. Configure Git to use .githooks directory for hooks
git config core.hooksPath .githooks
echo -e "  ✅ Configured Git core.hooksPath to '.githooks'."

echo -e "\n${BOLD}${GREEN}🎉 SUCCESS: Git Pre-Commit Hooks are now active!${NC}"
echo -e "Your slide presentations are now fully protected from structural and compilation breaks.\n"
