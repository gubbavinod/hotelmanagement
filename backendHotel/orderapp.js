import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

const OrderApp = () => {
    const [items, setItems] = useState([]);
    const [currentView, setCurrentView] = useState('past-orders');

    useEffect(() => {
        const loadItemsForNewOrder = async () => {
            try {
                const response = await fetch('/get_all_items');
                const data = await response.json();
                setItems(data);
            } catch (error) {
                console.error('Error fetching items:', error);
            }
        };

        // Simulated data for 'Past Orders' table
        // This will be fetched from Django later
        const pastOrdersData = [
            // Sample past orders data
        ];
        // Set past orders data
        // Your code here

        loadItemsForNewOrder();
    }, []);

    const handleViewChange = (view) => {
        setCurrentView(view);
    };

    const handleQuantityChange = (id, action) => {
        const updatedItems = items.map(item => {
            if (item.meal_id === id) {
                if (action === 'increment') {
                    return { ...item, quantity: (item.quantity || 0) + 1 };
                } else if (action === 'decrement' && (item.quantity || 0) > 0) {
                    return { ...item, quantity: (item.quantity || 0) - 1 };
                }
            }
            return item;
        });
        setItems(updatedItems);
    };

    return (
        <div>
            
            <div>
                <div onClick={() => handleViewChange('past-orders')}>Past Orders</div>
                <div onClick={() => handleViewChange('create-order')}>Create New Order</div>
            </div>
            {currentView === 'past-orders' && (
                <table>
                    <thead>
                        <tr>
                            <th>Order ID</th>
                            <th>Customer Name</th>
                            <th>Ordered Items Count</th>
                            <th>Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {/* Render past orders data here */}
                    </tbody>
                </table>
            )}
            {currentView === 'create-order' && (
                <table>
                    <thead>
                        <tr>
                            <th>Meal ID</th>
                            <th>Meal Name</th>
                            <th>Price</th>
                            <th>Quantity</th>
                        </tr>
                    </thead>
                    <tbody>
                        {items.map(item => (
                            <tr key={item.meal_id}>
                                <td>{item.meal_id}</td>
                                <td>{item.category}</td>
                                <td>${item.price}</td>
                                <td>
                                    <button onClick={() => handleQuantityChange(item.meal_id, 'decrement')}>-</button>
                                    <span>{item.quantity || 0}</span>
                                    <button onClick={() => handleQuantityChange(item.meal_id, 'increment')}>+</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
};

ReactDOM.render(<OrderApp />, document.getElementById('root'));
