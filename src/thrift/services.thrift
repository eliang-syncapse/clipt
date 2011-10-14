struct Snippet {
    1: string key,
    2: string value
}

service CliptService {
    Snippet read(1: string key),
    bool write(1: string key, 2: string value)
}
