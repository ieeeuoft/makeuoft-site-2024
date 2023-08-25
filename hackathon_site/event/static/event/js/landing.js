// Change navbar color on scroll
$(document).scroll(function () {
    let $nav = $(".navbar");
    $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
});

// Background color changing
$(window)
    .scroll(function () {
        let $window = $(window),
            $wrapper = $(".wrapper"),
            $colorScrollPanel = $(".colorScroll"),
            fontColors = ["#333", "#FFF", "#FFF", "#333", "#333"];

        // Change 40% earlier than scroll position so colour is there when you arrive.
        let scroll = $window.scrollTop() + $window.height() * 0.4;
        if ($window.scrollTop() < 300) {
            $wrapper.css("background-color", "#fff");
        }
        $colorScrollPanel.each(function (i) {
            let $this = $(this);

            if (
                $this.position().top <= scroll &&
                $this.position().top + $this.height() > scroll
            ) {
                $wrapper.css("background-color", $(this).attr("data-background-color"));
                $colorScrollPanel.css("color", fontColors[i]);
            }
        });
    })
    .scroll();

$(document).ready(function () {
    // Materialize stuff
    $(".carousel").carousel({ dist: 0, padding: 600 });
    setInterval(function () {
        $(".carousel").carousel("next");
    }, 3000);

    $(".scrollspy").scrollSpy();
    $(".collapsible").collapsible({ accordion: false });

    // Countdown stuff

    const now = new Date();
    let countDownDate;

    // Set the title based off what it's counting down to
    if (registrationOpenDate >= now) {
        countDownDate = registrationOpenDate;
        $("#countdownTitle").html("Registration Opens In");
    } else if (registrationCloseDate >= now) {
        countDownDate = registrationCloseDate;
        $("#countdownTitle").html("Registration Closes In");
    } else if (eventStartDate >= now) {
        countDownDate = eventStartDate;
        $("#countdownTitle").html("Event Starts In");
    }

    // Delete the entire countdown if event start date has passed
    if (eventStartDate < now) {
        $("#countdown").remove();
        $("#aboutText").removeClass("l7");
    } else {
        // Update the countdown every ten minute
        setInterval(setCounter(countDownDate), 600000);
    }
});

function setCounter(countDownDate) {
    const now = new Date();
    const distance = countDownDate - now;
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor(distance / (1000 * 60 * 60));

    console.log("days, hours", days, hours);

    if (hours < 1) {
        console.log("less than 1 hour");
        const minutes = Math.floor(distance / (1000 * 60));
        // Change to show minutes on the website
        $("#day1").parent().remove();
        $("#day2").html(Math.floor(minutes / 10));
        $("#day3").html(minutes % 10);
        $("#countdownUnit").html(minutes === 1 ? "Minute" : "Minutes");
        return;
    }

    if (days < 2) {
        console.log("less than 2 days");
        // Change to show hours on the website
        $("#day1").parent().remove();
        $("#day2").html(Math.floor(hours / 10));
        $("#day3").html(hours % 10);
        $("#countdownUnit").html(hours === 1 ? "Hour" : "Hours");
        return;
    }

    // Check if we need a third digit or not
    if (days > 99) {
        $("#day1").html(Math.floor(days / 100));
    } else {
        $("#day1").parent().remove();
    }

    $("#day2").html(Math.floor(days / 10) % 10);
    $("#day3").html(days % 10);
}
