var DELAY_TIME = 5000;

$(document).ready(function() {
    $("#upArrow").click(function() {
        $.get("/controls/forward")
    })
    $("#downArrow").click(function() {
        $.get("/controls/backward")
    })
    $("#rightArrow").click(function() {
        $.get("/controls/right")
    })
    $("#leftArrow").click(function() {
        $.get("/controls/left")
    })
    $("#stop").click(function() {
        $.get("/controls/stop")
    })
    $.get("/data/ip", (data) => {
        $("#ip").text(data)
    })
    setInterval(() => {
        $.get("/data/distance", (data) => {
            $("#distance").text(data)
        })
    }, DELAY_TIME);
    setInterval(() => {
        $.get("/data/cpu-temp", (data) => {
            $("#temperature").text(data)
        })
    }, DELAY_TIME);
    setInterval(() => {
        $.get("/data/cpu-usage", (data) => {
            $("#cpu").text(data)
        })
    }, DELAY_TIME);
})