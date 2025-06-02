import requests
import json

# Replace these with your actual Notion token and database ID
NOTION_TOKEN = "ntn_V58549764079g7nkZjeZzn13N0U5H24vL13MkQT6qR06Hb"
DATABASE_ID = "19c15cfb-d997-801f-804a-e9fe6116a934"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def create_page(data: dict):
    """
    Create a new page in the Notion database.
    """
    create_url = "https://api.notion.com/v1/pages"
    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": data
    }
    response = requests.post(create_url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Page created successfully.")
    else:
        print(f"Failed to create page: {response.status_code}")
        print(response.text)
    return response

def read_database():
    """
    Query and read pages from the Notion database.
    """
    read_url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(read_url, headers=headers)
    if response.status_code == 200:
        print("Database read successfully.")
        data = response.json()
        for result in data.get("results", []):
            print(f"Page ID: {result['id']}")
    else:
        print(f"Failed to read database: {response.status_code}")
        print(response.text)
    return response

def update_page(page_id: str, data: dict):
    """
    Update an existing page in the Notion database.
    """
    update_url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = {
        "properties": data
    }
    response = requests.patch(update_url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Page updated successfully.")
    else:
        print(f"Failed to update page: {response.status_code}")
        print(response.text)
    return response

def delete_page(page_id: str):
    """
    Delete (archive) a page in the Notion database.
    """
    delete_url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = {
        "archived": True
    }
    response = requests.patch(delete_url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Page deleted (archived) successfully.")
    else:
        print(f"Failed to delete page: {response.status_code}")
        print(response.text)
    return response

# Example usage:

# Define the properties for the new page
new_page_data = {
    "Name": {
        "title": [
            {
                "text": {
                    "content": "New Learning Resource"
                }
            }
        ]
    },
    "Content Type": {
        "select": {
            "name": "Courses"  # or "Books", "Video", etc.
        }
    },
    "Category": {
        "select": {
            "name": "Programming"
        }
    },
    "Resource": {
        "url": "https://example.com"
    },
    "Target": {
        "number": 100
    },
    "Completion": {
        "number": 0
    }
}

# Create a new page
create_response = create_page(new_page_data)
created_page_id = create_response.json().get("id")

# Read the database
read_database()

# Update the page
if created_page_id:
    updated_data = {
        "Title": {
            "title": [
                {
                    "text": {
                        "content": "Updated Sample Page"
                    }
                }
            ]
        }
    }
    update_page(created_page_id, updated_data)

# Delete the page
if created_page_id:
    delete_page(created_page_id)
