import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to my CV bot, "
        "\nI'm Mohammed F. Alhaddad, "
        "please write /help to see all commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'For Personal information, write: \n/personal_information'
        '\nFor LinkedIn URL, write: /linkedin'
        '\nFor GitHub URL, write: /github'
        '\nFor Summary, write: /summary'
        '\nFor Education, write: /education'
        '\nFor Certifications, write: /certifications'
        '\nFor Projects, write: /projects'
        '\nFor Soft skills, write: /soft_skills'
        '\nFor Software skills, write: /software_skills'
        '\nFor Languages, write: /languages'
    )

async def personal_information(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Name: Mohammed Fahim Alhaddad'
        '\nLocation: Riyadh City'
        '\nE-mail: malhaddad765@gmail.com'
        '\nPhone Number: +966590507998'
    )

async def linkedin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'My LinkedIn page:'
        '\nwww.linkedin.com/in/mohammed-f-alhaddad-945a7b311'
    )

async def github(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'My GitHub page:'
        '\nhttps://github.com/Mohammed-Alhaddad2003'
    )

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'A spiring senior computer science student with a passion for software development '
        'and a good foundation in programming languages including Java, Python,, etc. '
        'Seeking an internship opportunity to apply problem-solving skills, '
        'enhance coding proficiency, '
        'and contribute to innovative software projects within a dynamic tech company.'
    )

async def education(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Bachelor of Computer Science'
        '\nIslamic University in Medinah'
        '\n08/2021 - now'
    )

async def certifications(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Introduction of Artificial Intelligence'
        '\nKAUST Academy'
        '\n11/2023'
    )

async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Arabic tweets Analysis,'
        '\nA python script that analyzes tweets as input and then outputs the result as a positive or negative tweet, '
        'the algorithm that has been used for analyzing the tweets is the Naive Bayes Algorithm.'
        '\n\nYouTubeDownloader,'
        '\nA simple website that allows you to download any YouTube video in the highest quality by pasting the YouTube video link only,'
        'coded in Python, HTML, CSS'
        '\n\nLiveStream app,'
        '\nA python script that starts a live video stream from the streamer to clients, '
        'using multiple libraries such as socket, threading, json, base64, etc.'
        '\n\nCalculator'
        '\nA desktop application that calculates addition, multiplication, subtraction, and division between two numbers,'
        'coded in Python'
    )

async def soft_skills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'My soft skills are:'
        '\n- Communication'
        '\n- Teamwork'
        '\n- Problem solving'
        '\n- Emotional intelligence'
        '\n- Creativity'
        '\n- Critical thinking'
        '\n- Time management'
        '\n- Decision making'
    )

async def software_skills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'My software skills are:'
        '\n- Programming languages'
        '\nPython, Java, HTML, CSS, Dart'
        '\n\n- Database'
        '\nNoSQL'
        '\n\n- Microsoft products'
        '\nWord, Excel, PowerPoint'
    )

async def languages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'My languages are:'
        '\n- Arabic (Native language)'
        '\n- English'
    )

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Sorry, '{update.message.text}' is not a valid command"
    )

async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Sorry, I can't recognize you, you said '{update.message.text}'"
    )

def main():
    application = Application.builder().token("7287475698:AAE35DEPK2bzgvfq09qLZluUiqzgfUWhOE8").build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("personal_information", personal_information))
    application.add_handler(CommandHandler("linkedin", linkedin))
    application.add_handler(CommandHandler("github", github))
    application.add_handler(CommandHandler("summary", summary))
    application.add_handler(CommandHandler("education", education))
    application.add_handler(CommandHandler("certifications", certifications))
    application.add_handler(CommandHandler("projects", projects))
    application.add_handler(CommandHandler("soft_skills", soft_skills))
    application.add_handler(CommandHandler("software_skills", software_skills))
    application.add_handler(CommandHandler("languages", languages))

    # Message handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_text))

    # Unknown command handler
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Start the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()