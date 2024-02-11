// Expose function to Python 
// Python will be able to generate boards on command
eel.expose(replaceInnerHTML);
    
// Replaces body inner HTML with HTLM from argument
function replaceInnerHTML(x) {
    document.body.innerHTML = x;
}



