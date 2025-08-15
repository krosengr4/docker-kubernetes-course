const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;
const url = `http://localhost:${port}`;

const users = [];


app.use(bodyParser.json());
  
app.get('/', (req, res) => {
    res.send('Hello world!');
});

// Get registered users
app.get('/users', (req, res) => {
    return res.json({ users });
})

// Register a new user
app.post('/users', (req, res) => {
    const userId = req.body.userId;
    if (!userId) {
        return res.status(400).send('Missing User ID!');
    }

    if (users.includes(userId)) {
        return res.status(400).send('User already exists!')
    }

    users.push(userId);
    return res.status(201).send('User registered!')
})

app.listen(port, () => {
    console.log(`Server listening at ${url}`)
})