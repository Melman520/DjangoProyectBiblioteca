function toastify(text, color){
    Toastify({
        text: text,
        duration: 3200,
        destination: "",
        newWindow: true,
        close: false,
        gravity: "top", // `top` or `bottom`
        position: "center", // `left`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        style: {
            background: color
    },
        onClick: function () { } // Callback after click
    }).showToast();
}