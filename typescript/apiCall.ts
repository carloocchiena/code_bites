interface User {
        name: string
        age: string
}

function getUsers(): Promise<User[]> {

        // For now, consider the data is stored on a static `users.json` file
        return fetch('/users.json')
                // the JSON body is taken from the response
                .then(res => res.json())
                .then(res => {
                        // The response has an `any` type, so we need to cast
                        // it to the `User` type, and return it from the promise
                        return res as User[]
                })
}

const result = document.getElementById('result')
getUsers()
        .then(users => {
                result.innerHTML = users.map(u => u.).toString()
        })
  
