
4. Chrome Extension Content Script

The content script scans webpage text and interacts with the NLP model to highlight biased content.


document.addEventListener("DOMContentLoaded", () => {

    let paragraphs = document.querySelectorAll("p");

    paragraphs.forEach((p) => {

        let text = p.innerText;

        fetch("http://localhost:5000/analyze", {

            method: "POST",

            headers: { "Content-Type": "application/json" },

            body: JSON.stringify({ text: text }),
        })

        .then(response => response.json())

        .then(data => {

            if (data.biased_words.length > 0) {

                p.style.backgroundColor = "yellow";
            }
        });
    });
});
