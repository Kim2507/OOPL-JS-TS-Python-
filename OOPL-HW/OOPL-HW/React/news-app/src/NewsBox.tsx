import React ,{Component} from 'react';
//import "./NewsBox.css";
import BreakingNews from "./BreakingNews";
//import CardHeader from "./CardHeader";
//import CardContent from "./CardContent";
//import CardImage from "./CardImage";

/**
 * NewsBox Component.
 */
export class NewsBox extends Component {
	/**
	 * Render JSX Content.
	 * @returns JSX Element.
	 */
	render(){
		return (
			<div className="newsbox">
                <h1 className="title">News Box</h1>
                <BreakingNews/>
				
			</div>
		);
	}
}

export default NewsBox;