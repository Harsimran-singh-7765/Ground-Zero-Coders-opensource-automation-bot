## Github organization invite automation tool using requests 


## ⚙️ Setup Instructions

### **1️⃣ Create `.env` File**

In your project directory, add a file named `.env` with the following content:

```env
GITHUB_API_KEY=your_personal_access_token_here
ORG_NAME=your_organization_name_here
```
---

### 2️⃣ Prepare `members.xlsx`

Create an Excel file named `members.xlsx` with the following format:

| GitHubUsername   |
|------------------|
| harsimran-coder  |
| simran-dev123    |
| opensource-user  |

- Only valid GitHub usernames should be listed
- No empty rows or special characters

---

### 3️⃣ Install Requirements

Run the following command to install necessary dependencies:
```bash
pip install -r requirements.txt
```
---

### 4️⃣ Run the Bot

Execute the Python script:
```bash
python app.py
```

The script will:

✅ Read `.env` for token and organization name  
✅ Read usernames from `members.xlsx`  
✅ Send invites to your GitHub Organization  
✅ Display success or error messages  

---

## 🎉 That's It!
