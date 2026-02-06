import React from 'react';
import Modal from 'react-modal';

const UserDetailsModal = ({ isOpen, onRequestClose, user }) => {
    if (!user) return null;

    return (
        <Modal isOpen={isOpen} onRequestClose={onRequestClose} ariaHideApp={false}>
            <h2>User Details</h2>
            <button onClick={onRequestClose}>Close</button>
            <div>
                <h3>{user.name}</h3>
                <p>Email: {user.email}</p>
                <p>Submissions:</p>
                <ul>
                    {user.submissions.map(submission => (
                        <li key={submission.id}>{submission.title}</li>
                    ))}
                </ul>
            </div>
        </Modal>
    );
};

export default UserDetailsModal;