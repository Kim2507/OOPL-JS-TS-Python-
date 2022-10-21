import TaskEntry from "./TaskEntry";

/**
 * TodoList Data Interface.
 */

// State 
 interface TodoList {
	currentText: string;
	taskList: TaskEntry[];
	
}

export default TodoList;