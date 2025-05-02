document.addEventListener('DOMContentLoaded', function() {
    const scoreElement = document.getElementById('score');
    const biasArrow = document.getElementById('bias-arrow');

    // Get selected text from URL if available
    const urlParams = new URLSearchParams(window.location.search);
    const selectedTextFromPopup = urlParams.get('text');
    
    if (selectedTextFromPopup) {
        console.log('Selected text in popup:', selectedTextFromPopup);
        // Process the selected text and update UI
        analyzeText(selectedTextFromPopup);
    } else {
        // Default display if no text is selected
        scoreElement.textContent = "Select text to analyze";
        biasArrow.style.left = "50%"; // Center the arrow by default
    }

    // Add keyboard shortcut hint
    if (!selectedTextFromPopup) {
        scoreElement.textContent = "Select text and press Ctrl+Shift+V (or Command+Shift+V on Mac) to analyze";
    }

    const prefsBtn = document.getElementById('prefsBtn');
    const prefsModal = document.getElementById('prefsModal');
    const savePrefs = document.getElementById('savePrefs');
    const closePrefs = document.getElementById('closePrefs');

    // Open modal
    prefsBtn.addEventListener('click', () => {
        prefsModal.style.display = 'block';
    });

    // Close modal with close button
    closePrefs.addEventListener('click', () => {
        prefsModal.style.display = 'none';
    });

    // Close modal
    window.addEventListener('click', (event) => {
        if (event.target === prefsModal) {
            prefsModal.style.display = 'none';
        }
    });

    // Save preferences
    savePrefs.addEventListener('click', () => {
        const selectedMagazines = [...document.querySelectorAll('.magazine-list input:checked')]
            .map(input => input.value);
        
        // Save to chrome storage
        chrome.storage.sync.set({ 
            preferredMagazines: selectedMagazines 
        }, () => {
            prefsModal.style.display = 'none';
        });
    });
});

function analyzeText(text) {
    const scoreElement = document.getElementById('score');
    const biasArrow = document.getElementById('bias-arrow');

    // Placeholder for text analysis (you can replace this with actual API calls or logic)
    scoreElement.textContent = `Analyzing: "${text}" - 85% (Highly Credible)`;

    // Placeholder for bias meter (example: position at "Center Right")
    const biasPosition = "center-right"; // Options: "left", "center-left", "center", "center-right", "right"
    const positions = {
        "left": "10%",
        "center-left": "30%",
        "center": "50%",
        "center-right": "70%",
        "right": "90%"
    };
    biasArrow.style.left = positions[biasPosition];
}