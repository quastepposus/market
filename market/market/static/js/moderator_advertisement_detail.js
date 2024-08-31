const url = window.location.origin + '/api/advertiesments/'

async function accept () {
    const id = document.getElementById('adId').innerText
    const link = url + id + '/status/'
    const response = await fetch(link, {
        method: 'POST',
        headers: {
            'X-CSRFToken': Cookies.get('csrftoken')
        }
    })

    return response.json()
}

async function reject () {
    const id = document.getElementById('adId').innerText
    const link = url + id + '/status/'
    const response = await fetch(link, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': Cookies.get('csrftoken')
        }
    })
}


document.getElementById('accept').addEventListener('click', async () => {
    const response = await accept()
    console.log(response)

    window.location.pathname = '/moderators/advertisements/'
})

document.getElementById('reject').addEventListener('click', async () => {
    await reject()

    window.location.pathname = '/moderators/advertisements/'
})