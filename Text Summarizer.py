import nltk
import heapq
import tkinter as tk
from tkinter import ttk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Function to summarize text
def summarize_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        summary_output.config(text="⚠️ Please enter some text.", foreground="red")
        return

    try:
        sentences = sent_tokenize(text)
        words = word_tokenize(text.lower())
        stop_words = set(stopwords.words("english"))
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

        word_freq = {}
        for word in filtered_words:
            word_freq[word] = word_freq.get(word, 0) + 1

        sentence_scores = {}
        for sent in sentences:
            for word in word_tokenize(sent.lower()):
                if word in word_freq:
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word]

        summary_sentences = heapq.nlargest(2, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)

        summary_output.config(text="📝 Summary:\n" + summary, foreground="black")
    except Exception as e:
        summary_output.config(text="Error: " + str(e), foreground="red")
def clear_text():
    input_text.delete("1.0", tk.END)
    summary_output.config(text="")


# GUI Setup
window = tk.Tk()
window.title("😊 Text Summarizer")
window.geometry("600x550")
window.configure(bg="#f2f2f2")

# Heading
heading = tk.Label(window, text=" Text Summarizer", font=("Helvetica", 18, "bold"), bg="#f2f2f2", fg="#333")
heading.pack(pady=10)

# Frame for input
input_frame = tk.Frame(window, bg="#f2f2f2")
input_frame.pack(pady=5)

input_label = tk.Label(input_frame, text="Enter your text below:", font=("Arial", 12), bg="#f2f2f2")
input_label.pack(anchor="w")

input_text = tk.Text(input_frame, height=10, width=70, font=("Arial", 11), bd=2, relief="groove", wrap="word")
input_text.pack(pady=5)

# Summarize Button
summarize_button = tk.Button(window, text="🔍 Summarize", command=summarize_text,
                             font=("Arial", 12, "bold"), bg="#4a90e2", fg="white", relief="raised", bd=2,
                             padx=10, pady=5)
summarize_button.pack(pady=10)
clear_button = tk.Button(window, text="🗑️ Clear", command=clear_text,
                         font=("Arial", 12), bg="#e74c3c", fg="white",
                         relief="raised", bd=2, padx=10, pady=5)
clear_button.pack(pady=5)


# Output
summary_output = tk.Label(window, text="", font=("Arial", 11), wraplength=550, justify="left", bg="#f2f2f2")
summary_output.pack(pady=10)

# Footer
footer = tk.Label(window, text="✨ Made by Priyanshi Gupta ✨", font=("Arial", 10, "italic"),
                  fg="#777", bg="#f2f2f2", anchor="e")
footer.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)  # Bottom-right corner with margin

# Run the GUI
window.mainloop()
