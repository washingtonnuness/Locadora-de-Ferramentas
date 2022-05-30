var id_tipo = document.getElementById("id_tipo");
window.onload = function getElement(id_tipo) {
    
    //getElement(id_tipo)
	// var label = document.getElementById("div_id_locomocao").style.display = 'none';
	// var field = document.getElementById('id_locomocao').style.display = 'none';
    oculta("inputRg")
    oculta("inputCpf")
    oculta("inputClient")

}

function getElement(id_tipo){
	if(id_tipo == 'CPF') {
        exibe("inputRg")
        exibe("inputCpf")
        exibe("inputClient")
        oculta("inputRegistro")
        oculta("inputRazao")
        oculta("inputNameFant")

		}else{
            oculta("inputRg")
            oculta("inputCpf")
            oculta("inputClient")
            exibe("inputRegistro")
            exibe("inputRazao")
            exibe("inputNameFant")
		}
};

function exibe(element){
    var fild = document.getElementById(element)
        fild.style.display = 'block'
}

function oculta(element){
    var fild = document.getElementById(element)
        fild.style.display = 'none'

}