import "./App.css";
import TodoTable from "./TodoTable";
import TaskEntry from "./TaskEntry";
import TaskEntryPanel from "./TaskEntryPanel";
import React from "react";
import TodoList from "./TodoList";

/**
 * TodoListPanel Component.
 */
class TodoListPanel extends React.Component<{}, TodoList> {
	/**
	 * Initialize Log State.
	 */
	constructor(props: {}) {
		super(props);
		this.state = {
			currentText: "",
			taskList: [],
			
		};

		// This binding is necessary to make `this` work in the callback
		this.textHandler = this.textHandler.bind(this);
		this.addTaskHandler = this.addTaskHandler.bind(this);
		this.deleteTaskEntryHandler = this.deleteTaskEntryHandler.bind(this);
		this.toggleDoneTaskEntryHandler = this.toggleDoneTaskEntryHandler.bind(this);
		
		
	}

	/**
	 * Render JSX Content.
	 * @returns JSX Element.
	 */
	render(): JSX.Element {
		return (
			<div>
				<h1 className="post-title">Todo List</h1>
				<div>
					<TaskEntryPanel 
						currentText={this.state.currentText}
						textHandler={this.textHandler}
						addTaskHandler={this.addTaskHandler}/>
				</div>
				<p/>
				<div className="pure-u-1-2">
					<TodoTable 
						taskList={this.state.taskList}
						deleteTaskEntryHandler = {this.deleteTaskEntryHandler}
						toggleDoneTaskEntryHandler = {this.toggleDoneTaskEntryHandler}
						 />
				</div>
			</div>
		);
	}

	/**
	 * Triggered when user enters text into the Text Box.
	 */
	textHandler(event: React.FormEvent<HTMLInputElement>) {
		let newTextValue = event.currentTarget.value;
		console.log("Got Text Change:  " + newTextValue);
		let todoList = this.state.taskList;
		this.setState({
			currentText: newTextValue,
			taskList: todoList,
		});
	}

	/**
	 * Triggered when user clicks the Add Button.
	 */
	addTaskHandler() {
		let todoList = this.state.taskList;
		
		if (this.state.currentText) {
			console.log("Adding new journal item:  " + this.state.currentText);
			let currentTime = new Date();
			let newEntry: TaskEntry = {
				timeStamp: currentTime,
				textEntry: this.state.currentText,
				status:"Pending",
			};
			todoList.push(newEntry);
			
			this.setState({
				currentText: "",
				taskList: todoList,
			});
		}
	}

	/**
	 * Triggered when user wants to delete an entry.
	 */
	deleteTaskEntryHandler(index: number) {
		console.log("Deleting Task Entry:  " + index);
		let todoList = this.state.taskList;
		
		// Note that there is no remove method in JavaScript; we use splice instead.
		// Remove the task 
		todoList.splice(index, 1);
		this.setState({
			currentText: this.state.currentText,
			taskList: todoList,
		});
	}

	/**
	 * Triggered when user wants to mark the task done.
	 */

	toggleDoneTaskEntryHandler(index: number) {
		console.log("Mark task done:  " + index);
		let todoList = this.state.taskList;
		//Mark the selected task as Done
		todoList[index].status="Done";
		this.setState({
			currentText: this.state.currentText,
			taskList: todoList,
			
		});
	}
}

export default TodoListPanel;
