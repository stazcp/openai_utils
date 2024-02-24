from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def delete_all_assistants():
    try:
        # Fetch the list of all assistants with a limit of 100
        my_assistants = client.beta.assistants.list(
            order="desc",
            limit=100  # Adjust the limit to 100
        )

        # Check the structure of my_assistants and adapt accordingly
        for assistant in my_assistants.data:
            # Access attributes with dot notation if necessary
            assistant_id = assistant.id  # Use .id instead of ['id'] if the objects are not dictionaries
            delete_response = client.beta.assistants.delete(assistant_id)
            print(f"Deleted assistant {assistant_id}: {delete_response}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to delete all assistants
delete_all_assistants()
