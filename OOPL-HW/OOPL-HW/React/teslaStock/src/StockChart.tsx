import { screen } from "@testing-library/react";
import React from "react";
import { VictoryLine, VictoryChart, VictoryTheme, VictoryAxis} from "victory";

/**
 * Basic LineChart Component.
 */
 


 interface stockPrice{
	data:number[]
 }


class StockChart extends React.Component<stockPrice>{
	/**
	 * Render JSX Content.
	 * @returns JSX Element.
	 */

	render(): JSX.Element {

        
		
		return (
			<div className="victory_chart">
				<VictoryChart theme={VictoryTheme.material}>
					<VictoryLine data={this.props.data}/>
                </VictoryChart>
			</div>
		);
	}
}

export default StockChart;
