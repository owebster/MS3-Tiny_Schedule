function sendMail(contactForm){
    emailjs.send("service_9sp6wie", "template_p4l7sii", {
        "from_name": contactForm.from_name.value,
        "from_email": contactForm.from_email.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("success", response);
        },
        function(error) {
            console.log("fail", error);
        });
    return false;
}