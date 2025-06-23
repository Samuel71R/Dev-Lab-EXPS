import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import warnings
warnings.filterwarnings("ignore")

# ------------------------------
# STEP 1: Create Sample Data
# ------------------------------
data = {
    'subject': [
        "Hello", "Win iPhone", "Meeting Reminder", "Free Coupons", "Lunch?", "Project Update", 
        "You Won!", "Invoice Attached", "Weekend Plans", "Important Notification"
    ],
    'sender': [
        "john@example.com", "spam@offers.com", "boss@company.com", "deal@promo.com",
        "friend@example.com", "manager@work.com", "lottery@scam.com", "billing@company.com",
        "friend@example.com", "notice@alerts.com"
    ],
    'content': [
        "Hi, how are you?", "You have won an iPhone!", "Meeting at 3PM in Room 1",
        "Claim your free coupon now", "Want to grab lunch today?", "Updated the project files",
        "Congratulations, you won!", "Your invoice is attached", "Plans for the weekend?",
        "Account alert: verify now"
    ],
    'timestamp': [
        "2023-08-01 10:00:00", "2023-08-01 11:30:00", "2023-08-01 14:00:00", "2023-08-02 09:00:00",
        "2023-08-02 12:30:00", "2023-08-03 16:00:00", "2023-08-03 17:45:00", "2023-08-04 08:15:00",
        "2023-08-04 19:00:00", "2023-08-05 13:10:00"
    ],
    'label': [
        "ham", "spam", "ham", "spam", "ham", "ham", "spam", "ham", "ham", "spam"
    ]
}

df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.day_name()

# ------------------------------
# STEP 2: Basic Info
# ------------------------------
print("\n🔍 Shape:", df.shape)
print("\n🧾 Columns:", df.columns.tolist())
print("\n📊 Head:\n", df.head())
print("\n🧹 Missing:\n", df.isnull().sum())

# ------------------------------
# STEP 3: Label Distribution
# ------------------------------
sns.countplot(x='label', data=df)
plt.title("Label Distribution")
plt.show()

# ------------------------------
# STEP 4: Emails per Hour
# ------------------------------
plt.figure(figsize=(8, 4))
sns.histplot(df['hour'], bins=24)
plt.title("Emails by Hour")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.show()

# ------------------------------
# STEP 5: Emails by Day
# ------------------------------
plt.figure(figsize=(8, 4))
sns.countplot(x='day_of_week', data=df, order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
plt.title("Emails by Day of Week")
plt.xticks(rotation=45)
plt.show()

# ------------------------------
# STEP 6: Top Senders
# ------------------------------
top_senders = df['sender'].value_counts().head(5)
plt.figure(figsize=(8, 4))
sns.barplot(x=top_senders.values, y=top_senders.index)
plt.title("Top Email Senders")
plt.xlabel("Count")
plt.ylabel("Sender")
plt.show()

# ------------------------------
# STEP 7: Word Clouds
# ------------------------------
spam_text = " ".join(df[df['label'] == 'spam']['content'])
ham_text = " ".join(df[df['label'] == 'ham']['content'])

spam_wc = WordCloud(width=500, height=300, background_color='white').generate(spam_text)
ham_wc = WordCloud(width=500, height=300, background_color='white').generate(ham_text)

plt.imshow(spam_wc, interpolation='bilinear')
plt.axis("off")
plt.title("Spam Word Cloud")
plt.show()

plt.imshow(ham_wc, interpolation='bilinear')
plt.axis("off")
plt.title("Ham Word Cloud")
plt.show()