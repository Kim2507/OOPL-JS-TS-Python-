import React from "react";
import "./App.css";

/**
 * TaskEntry Props.
 */
 interface TaskEntryProps {
	currentText: string;

	// Define Event Handlers
	textHandler: (event: React.FormEvent<HTMLInputElement>) => void;
	addTaskHandler: () => void;
}


/**
 * TaskEntryPanel Component.
 */
class TaskEntryPanel extends React.Component<TaskEntryProps> {

	/**
	 * Render JSX Content.
	 * @returns JSX Element.
	 */
	render(): JSX.Element {
		return (
			<div>
				<input
					className="pure-u-12-24"
					type="text"
					onChange={this.props.textHandler}
					value={this.props.currentText}
				/>
				<p />
				<button
					className="pure-button pure-button-primary"
					onClick={this.props.addTaskHandler}
				>
					Add new task
				</button>
			</div>
		);
	}
}

export default TaskEntryPanel;