import streamlit as st

st.set_page_config(page_title="mentomoney", layout="centered")

st.markdown("""
<style>
    .reportview-container .markdown-text-container {
        text-align: right;
        direction: rtl;
    }
    .stTextInput > div > div > input {
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

st.title("💰 mentomoney – המנטור החכם שלך להתנהלות כלכלית")

st.markdown("""
ברוך הבא ל־**mentomoney** – סוכן הבינה המלאכותית שיעזור לך להבין, לחשב ולשפר את ההתנהלות הכלכלית שלך.
""")

st.subheader("📌 מה תרצה לעשות?")
option = st.selectbox("בחר תחום להתחלה:", [
    "💸 להבין את ההתנהלות הפיננסית שלי",
    "👨‍👩‍👧‍👦 לחנך את ילדיי להתנהלות כלכלית",
    "🔒 גישה לתוכן בלעדי למנויים"
])

if option == "💸 להבין את ההתנהלות הפיננסית שלי":
    st.header("💼 מחשבון מס הכנסה")
    salary = st.number_input("מה ההכנסה החודשית שלך (ברוטו)?", min_value=0)
    children = st.number_input("כמה ילדים יש לך?", min_value=0)
    age = st.number_input("בן/בת כמה אתה?", min_value=0)
    is_shahir = st.radio("האם אתה שכיר?", ["כן", "לא"])

    if st.button("חשב את המס"):
        base_tax = salary * 0.1
        credit = children * 223 + (age >= 60) * 220
        final_tax = max(base_tax - credit, 0)
        st.success(f"המס החודשי המשוער שלך: {final_tax:,.0f} ש״ח")

elif option == "👨‍👩‍👧‍👦 לחנך את ילדיי להתנהלות כלכלית":
    st.header("👪 חינוך פיננסי לילדים – לפי גיל")
    age_group = st.selectbox("גיל הילד/ה", ["4–6", "7–10", "11–14", "15–18"])

    if age_group == "4–6":
        st.markdown("""
        - משחקי חנות עם קופה
        - דיבור פשוט על כסף
        - התחלת הרגלי חיסכון
        """)
    elif age_group == "7–10":
        st.markdown("""
        - דמי כיס ומעקב
        - תקצוב רצונות קטנים
        - חשיבה על פרסומות
        """)
    elif age_group == "11–14":
        st.markdown("""
        - אחריות על קניות בבית
        - הסבר מושגים: ריבית, תקציב, תיעדוף
        """)
    elif age_group == "15–18":
        st.markdown("""
        - חשבון בנק לנוער
        - סימולציות תקציב
        - שיחה על אשראי ואחריות כלכלית
        """)

elif option == "🔒 גישה לתוכן בלעדי למנויים":
    st.header("🚧 בקרוב – אזור המנויים")
    st.info("פיצ'רים מתקדמים כמו סימולציות, תוכניות חסכון ודוחות חכמים ייפתחו למנויים בלבד.")

st.divider()
st.markdown("🤖 שיח פתוח עם mentomoney יתווסף בקרוב – כולל יכולת שיחה חופשית עם הסוכן בשפה טבעית.")
