//var myModal = document.getElementById('exampleModal')
////var myInput = document.getElementById('myInput')
//var closeButton = document.getElementById('close-button')
//
//closeButton.addEventListener('click', function () {
//  myModal.focus()
//})

let buttonArray = document.getElementsByClassName('btn-close');

let triggerFunc = function(){
    let productId = this.getAttribute("value");
    let productName = document.getElementById('header-' + productId);
    productName = productName.innerHTML;

    let modalHeader = document.getElementById('exampleModalLabel');
    modelHeader.innerHTML = productName;

    let modalButton = document.getElementById('deleteLink');
    modalButton.attr('href', '/delete' + productId);
}

for (let i = 0; 1 < buttonArray.length; i++){
    buttonArray[i].addEventListener('click', triggerFunc);
}
