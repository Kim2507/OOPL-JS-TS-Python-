import { getElementError } from "@testing-library/react";
import React from "react";
import { Border } from "victory";
import App from "./App";

interface stockPrice{
	data:number[]
 }

class StockTable extends React.Component<stockPrice>{
	/*
   * Render JSX Content.
	 * @returns JSX Element.
	 */
    
	render(): JSX.Element{
        const data= this.props.data
        const tableData=data.map(this.displayData)
        
		return (
			<div>
				
        <p/>
				<table  className="pure-table pure-table-bodered"
                style={{border: "3px solid rgb(0, 0, 0)"}}
                 >
					<thead>
						<tr>
							<th>Stock Close</th>
						</tr>
					</thead>
					<tbody>
                        <tr>
                            <td>{tableData}</td>
                        </tr>    
					</tbody>
          </table> 
			</div>
		);
	}

    displayData(price:number){
            return(
                <tr>
                    <td>{price}</td>
                </tr>
            )
    } 
}

export default StockTable;