const input = document.querySelector('#file');

function is_used (e) {
    is_used = this.files.length > 0

    if(is_used) {
        this.classList.add('active')
    } else {
        this.classList.remove('active')
    }
}

input.addEventListener('change', is_used)