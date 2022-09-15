

function makeCard(data){
    let htmlPlace = document.getElementById('data-cards')
    for (let item of data) {
        if (item['age'] === null){
            item['age'] = 'no data'
        }
        let card = document.createElement('div')
        let cardShowData = document.createElement('div')
        card.classList.add('data-card')
        card.dataset.alive = item['alive']
        card.innerHTML += item['name'] + " (" + item['age'] + ")"
        cardShowData.innerHTML += item['roles'] + ' shows'
        cardShowData.classList.add('data-card-shows')
        card.appendChild(cardShowData)
        htmlPlace.appendChild(card)
    }
    let cards = document.getElementsByClassName('data-card')
    mouseMove(cards)
}

function mouseMove(cards){
    for (let card of cards){
        card.addEventListener('mouseover', ()=>{
            if (card.dataset.alive === 'true' ){
                card.classList.add('alive')
            } else {
                card.classList.add('dead')
            }
        })
        card.addEventListener('mouseleave', ()=>{
            card.classList.remove('alive')
             card.classList.remove('dead')
        })
    }
}

async function getData(url){
    const response = await fetch(url)
    const data = await response.json()
    return makeCard(data)
}

getData('api/actors')