const express = require('express');
const app = express();

app.use(express.static('views'));
app.set('view engine', 'ejs');
app.set('views', './views');

app.get('/', (req, res) => {
    res.render('index');
});

app.listen(3001, () => {
    console.log('Server listening on port 3001');
});
