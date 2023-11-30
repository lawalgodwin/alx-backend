import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => console.log('connected server sucessfully'));
client.on('error', (err) => console.log('failed connecting to server', err.message));

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

const reserveStockById = (itemId, stock) => {
  const key = `item.${itemId}`;
  client.set(key, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  client.get = promisify(client.get);
  const key = `item.${Number(itemId)}`;
  const stock = await client.get(key);
  return stock;
};

const getItemById = (id) => {
  const [product] = listProducts.filter((item) => item.itemId === (id));
  return product;
};

const app = express();

app.get('/list_products', (req, res) => {
  res.status(200).json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  if (!currentStock) {
    await reserveStockById(itemId, item.initialAvailableQuantity);
    item.currentQuantity = item.initialAvailableQuantity;
  } else item.currentQuantity = currentStock;
  res.json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);

  const item = getItemById(itemId);

  if (!item) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }
  let availableStock = await getCurrentReservedStockById(itemId);
  if (!availableStock) availableStock = item.initialAvailableQuantity;
  if (availableStock < 1) {
    res.json({ status: 'Not enough stock available', itemId });
    return;
  }
  await reserveStockById(itemId, Number(availableStock) - 1);
  return res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(1245, () => console.log('server running on port 1245'));
