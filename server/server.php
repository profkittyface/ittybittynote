<?php
header("Access-Control-Allow-Origin: *");
$conn = pg_connect("host=localhost dbname=ittybittynote user=ahunt");

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['title'])) {
        $title = $_POST['title'];
    } else {
        echo "Missing title";
    };

    if (isset($_POST['content'])) {
        $content = $_POST['content'];
    } else {
        echo "Missing content";
    };

    $result = pg_query($conn, 'insert into notes (title,content) values ('.$title.','.$content.') returning id');
    echo json_encode($note_list, JSON_PRETTY_PRINT);
    exit;
};

if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    $result = pg_query($conn, 'select * from notes limit '.$limit);
    if (!$result) {
        echo "An error occured\n";
        exit;
    }
    $note_list = array();
    while ($row = pg_fetch_row($result)) {
        $note = array(
    "id" => "$row[0]",
    "title" => "$row[1]",
    "content" => "$row[2]",
    "created" => "$row[3]");

        $note_list[] = $note;
    };
    echo json_encode($note_list, JSON_PRETTY_PRINT);
};

// DROP TABLE IF EXISTS notes;
// CREATE TABLE notes
// (id serial PRIMARY KEY,
// title text,
// content text,
// created timestamp DEFAULT now(),
// modified timestamp DEFAULT now()
// );
// INSERT INTO notes (title,content) VALUES (E'shopping list', E'milk\neggs\nstuff');
// INSERT INTO notes (title,content) VALUES (E'stuff', 'milk\neggs\nstuff');
// INSERT INTO notes (title,content) VALUES (E'address list', '2343');
