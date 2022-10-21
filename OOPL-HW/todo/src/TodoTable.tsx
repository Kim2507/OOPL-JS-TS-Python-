import React from "react";
import "./App.css";
import TaskEntry from "./TaskEntry";

/**
 * Todo Table Props.
 */
interface TodoTableProps {
	taskList: TaskEntry[];
	deleteTaskEntryHandler: (index: number) => void;
	toggleDoneTaskEntryHandler: (index:number)=>void;
}

/**
 * TodoTable Component.
 */
class TodoTable extends React.Component<TodoTableProps> {
	/**
	 * Initializer.
	 */
	 constructor(todoTableProps: TodoTableProps) {
		super(todoTableProps);

		// This binding is necessary to make `this` work in the callback
		this.getTaskRow = this.getTaskRow.bind(this);
	}

	/**
	 * Render JSX Content.
	 * @returns JSX Element.
	 */
	render(): JSX.Element {
		let taskRows = this.props.taskList.map(this.getTaskRow);
		return (
			<table className="pure-table">
				<thead>
					<tr>
						<th>Status</th>
						<th>Timestamp</th>
						<th>Entry</th>
						<th>Action</th>
						<th>Action</th>
					</tr>
				</thead>
				<tbody>{taskRows}</tbody>
			</table>
		);
	}

	/**
	 * Gets the Journal Row.
	 */
	getTaskRow(item: TaskEntry, index: number) {
		return (
			<tr key={item.timeStamp.getSeconds()}>
				<td>
					{item.status}
				</td>

				<td>
					{item.timeStamp.toLocaleDateString()}{" "}
					{item.timeStamp.toLocaleTimeString()}
				</td>
				<td>{item.textEntry}</td>
				<td>
					
					<button
						className="pure-button"
						onClick={this.props.toggleDoneTaskEntryHandler.bind(this,index)}
					>
						Toggle Done
					</button>
				</td>
				<td>
					<button
						className="pure-button"
						onClick={this.props.deleteTaskEntryHandler.bind(this, index)}		
					>
						Delete
					</button>
				</td>

				
			</tr>
		);
	}
}

export default TodoTable;
