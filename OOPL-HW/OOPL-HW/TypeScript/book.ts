class Book{
    title : string;
    author: string;
    year_published: number;

    constructor(ttl: string, author:string, year_pub: number){
        this.title = ttl;
        this.author = author;
        this.year_published = year_pub;
    }

    setYear(year: number){
        if(year>1945 && year <2100)
            this.year_published = year;
        else throw new Error("The year is invalid");
    }

    getYear(){
        return this.year_published;
    }
}

let book = new Book("Be yourself","Alan",2000);
let book2 = new Book("Bop Bop","John",1900);
console.log(book);