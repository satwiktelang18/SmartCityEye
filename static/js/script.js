document.addEventListener("DOMContentLoaded", () => {

    const dropArea = document.getElementById("dropArea");
    const input = document.getElementById("videoInput");
    const fileName = document.getElementById("fileName");

    console.log("JS Loaded");
    console.log(dropArea);
    console.log(input);
    console.log(fileName);

    if (!dropArea || !input || !fileName) {
        console.error("HTML elements not found!");
        return;
    }

    // Click to browse
    dropArea.addEventListener("click", () => {
        input.click();
    });

    // Prevent browser opening file
    ["dragenter", "dragover", "dragleave", "drop"].forEach(event => {
        document.addEventListener(event, e => {
            e.preventDefault();
            e.stopPropagation();
        });
    });

    // Highlight drop area
    ["dragenter", "dragover"].forEach(event => {
        dropArea.addEventListener(event, () => {
            dropArea.classList.add("drag-active");
        });
    });

    ["dragleave", "drop"].forEach(event => {
        dropArea.addEventListener(event, () => {
            dropArea.classList.remove("drag-active");
        });
    });

    // Handle dropped file
    dropArea.addEventListener("drop", e => {

        const files = e.dataTransfer.files;

        if (files.length) {

            input.files = files;

            fileName.textContent = files[0].name;

        }

    });

    // Handle clicked file
    input.addEventListener("change", () => {

        if (input.files.length) {

            fileName.textContent = input.files[0].name;

        }

    });

});