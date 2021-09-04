let buttonArray = document.getElementsByClassName("button-card");

let triggerFunc = function(){
    let productId = this.getAttribute("value")
    let productName = document.getElementById("header-" + productId);
    productName = productName.innerHTML;

    let modalHeader = document.getElementById("exampleModalLabel");
    modalHeader.innerHTML = "Удалить " + productName + "?";

    let modalButton = document.getElementById("deleteLink");
    modalButton.setAttribute('href', '/delete/' + productId);
}

for (let i = 0; i < buttonArray.length; i++){
    buttonArray[i].addEventListener('click', triggerFunc);
}