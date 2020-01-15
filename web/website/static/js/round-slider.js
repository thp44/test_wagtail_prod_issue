$("#slider").roundSlider({
    radius: 120,
    max: 360,
    width: 20,
    handleSize: "25",
    handleShape: "round",
    startAngle: 90,
    endAngle: "+360",
    sliderType: "min-range",
    value: 180,
    create: function (args) {
        window.orientation = args.value;
    },
    change: function (args) {
            var orientation = args.value;
            window.orientation = args.value;
            $("#post-form").append("<input type='hidden' name='orientation' value='" + orientation + "'/>");
         }
    }
);
