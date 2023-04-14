const countEL = document.getElementById('count');

updateVisitCount();

function updateVisitCount() {
    fetch('https://api.countapi.xyz/update/aedla-gapop/website/?amount=1')
            .then(res => res.json())
            .then(res =>{
                countEL.innerHTML = res.value;
            })
}