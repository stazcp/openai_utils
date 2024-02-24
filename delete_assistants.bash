#!/bin/bash

OPENAI_API_KEY=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
# Ensure your OPENAI_API_KEY environment variable is set
if [ -z "$OPENAI_API_KEY" ]; then
  echo "OPENAI_API_KEY is not set. Please set it before running this script."
  exit 1
fi

while IFS= read -r assistant_id; do
  echo "Deleting assistant with ID: $assistant_id"
  curl https://api.openai.com/v1/assistants/$assistant_id \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -H "OpenAI-Beta: assistants=v1" \
    -X DELETE
  echo -e "\n" # New line for better readability in output
done < "assistant_ids.txt"