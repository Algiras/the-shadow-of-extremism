#!/bin/bash
# Fix QMD formatting - ensure blank lines before bullet lists

# This script will be used to identify patterns that need fixing
echo "QMD Formatting Rules:"
echo "1. Bullet lists MUST have a blank line before them"
echo "2. Use * or - for bullets, followed by a space"
echo "3. Bold text uses **text**"
echo "4. Italics use *text*"
echo ""
echo "Common pattern to fix:"
echo "BAD:  Some text"
echo "      *   **Bold**: Description"
echo ""
echo "GOOD: Some text"
echo ""
echo "      *   **Bold**: Description"
