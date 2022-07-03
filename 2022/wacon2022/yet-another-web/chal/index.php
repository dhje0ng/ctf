<?php
session_start();
if (!isset($_POST["url"])) {
    highlight_file(__FILE__);
}

function uuid()
{
    $chars = md5(uniqid(mt_rand(), true));
    $uuid = substr($chars, 0, 8) . '-'
        . substr($chars, 8, 4) . '-'
        . substr($chars, 12, 4) . '-'
        . substr($chars, 16, 4) . '-'
        . substr($chars, 20, 12);
    return $uuid;
}

function Check($url)
{
    $blacklist = "/\}|\{|\[|\]|\:|f|g|[\x01-\x1f]|[\x7f-\xff]|['\"]/i";
        # filtered }, {, [, ], :, f, g,

    if (is_string($url)
        && strlen($url) < 4096
        && !preg_match($blacklist, $url)) {
        return true;
    }
    return false;
}

if (!isset($_SESSION["uuid"])) {
    $_SESSION["uuid"] = uuid();
}

echo $_SESSION["uuid"]."</br>";

if ($_POST["url"]) {
    $url = escapeshellarg($_POST["url"]);
    $cmd = "/usr/bin/curl ${url} --output - -m 3 --connect-timeout 3";
    echo "your command: " . $cmd . "</br>";
    $res = shell_exec($cmd);
    echo $res;
} else {
    die("error~");
}

// if (strpos($res, $_SESSION["uuid"]) !== false) {
//     echo $res;
// } else {
//     echo "you cannot get the result~";
// }