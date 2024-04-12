function startCountdown() {
    var seconds = 20;
    var countdownInterval = setInterval(function() {
        document.getElementById("countdown").innerText = seconds + " seconds";
        seconds--;
        if (seconds < 0) {
            clearInterval(countdownInterval);
            window.alert("TIME UP");
            fetch("https://project.my-market.co.ke/Callback_main/CallbackResponse.json")
                .then((response) => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then((json) => console.log(json))
                .catch((error) => console.error('Error fetching data:', error));
        }
    }, 1000);
}
