#!/bin/bash
# update-models.sh - Simple script to update models.mdx from OpenAPI spec

echo "🔄 Updating models.mdx from OpenAPI specification..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if PyYAML is available
if ! python3 -c "import yaml" &> /dev/null; then
    echo "📦 Installing PyYAML..."
    pip3 install pyyaml
fi

# Run the generator
python3 generate_models.py

# Check if there are changes
if [ -n "$(git status --porcelain reference/models.mdx)" ]; then
    echo "✅ Models updated! Changes detected in reference/models.mdx"
    echo "💡 Run 'git add reference/models.mdx && git commit -m \"Update models from OpenAPI spec\"' to commit changes"
else
    echo "✅ Models are up to date!"
fi
