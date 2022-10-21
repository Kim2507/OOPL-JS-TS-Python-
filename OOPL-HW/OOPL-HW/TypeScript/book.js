var Book = /** @class */ (function () {
    function Book(ttl, author, year_pub) {
        this.title = ttl;
        this.author = author;
        this.year_published = year_pub;
    }
    Book.prototype.setYear = function (year) {
        if (year > 1945 && year < 2100)
            this.year_published = year;
        else
            throw new Error("The year is invalid");
    };
    Book.prototype.getYear = function () {
        return this.year_published;
    };
    return Book;
}());
var book = new Book("Be yourself", "Alan", 2000);
console.log(book);
