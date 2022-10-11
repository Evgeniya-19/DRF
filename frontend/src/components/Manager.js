import React from "react";

const ManagerItem = ({manager}) => {
    return (
        <tr>
            <td>{manager.first_name}</td>
            <td>{manager.last_name}</td>
            <td>{manager.user_name}</td>
            <td>{manager.email}</td>
        </tr>
    )
}

const ManagerList = ({managers}) => {
    return (
        <table>
            <th>First name</th>
            <th>Last Name</th>
            <th>User name</th>
            <th>Email</th>
            {managers.map((manager_) => <ManagerItem manager={manager_} />)}
        </table>
    )
}

export default ManagerList