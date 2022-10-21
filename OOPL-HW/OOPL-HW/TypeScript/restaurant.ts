class Restaurant{
    name: string;
    city : string;

    constructor(name:string, city:string){
        this.name= name;
        this.city= city;
    }
}

class IceCreamStand extends Restaurant{
private flavors : string[];
    constructor(name:string,city:string,flavors:string[]){
        
        super(name,city);
        this.flavors = flavors;
    }
}

let flavors = ["Vani","Chocolate","Mint"];
let icecream = new IceCreamStand("J&J","Boston",flavors);
console.log(icecream)