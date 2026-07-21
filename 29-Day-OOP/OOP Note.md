# Introduction to Object-Oriented Programming (OOP)

## Introduction

As programs become larger and more complex, organizing code becomes increasingly important.

**Object-Oriented Programming (OOP)** is a programming paradigm that helps organize and structure code by using **objects**. It makes programs more:

- Organized
- Reusable
- Maintainable
- Easier to understand

Instead of writing all code in one place, OOP allows you to group related **data** and **functions** together into a single unit called an **object**.

---

# What is OOP?

Imagine you're building with **LEGO® bricks**.

In procedural programming, you have a pile of individual bricks and manually assemble everything step by step.

In Object-Oriented Programming, you create complete objects, such as:

- 🚗 Car
- 🏠 House
- 🤖 Robot

Each object has its own **properties** and **behaviors**.

This makes programs easier to design and reuse.

---

# What is an Object?

An **object** is a real-world entity that contains:

- **Data (Attributes)** → Information about the object.
- **Actions (Methods)** → Things the object can do.

Think of an object as a self-contained unit that combines both data and behavior.

---

# Attributes (Data)

Attributes are the characteristics or properties of an object.

### Example: Car

A car can have the following attributes:

- Color
- Brand
- Model
- Speed
- Fuel Type

Example:

```text
Car
├── Color : Red
├── Brand : Toyota
├── Model : Corolla
└── Speed : 80 km/h
```

---

# Methods (Actions)

Methods are the actions or behaviors that an object can perform.

### Example: Car

A car can:

- Start
- Accelerate
- Brake
- Turn
- Stop

Example:

```text
Car
├── start()
├── accelerate()
├── brake()
├── turn()
└── stop()
```

---

# Real-Life Example

Consider a **Student** object.

### Attributes

- Name
- Roll Number
- Age
- Grade

### Methods

- Study
- Attend Class
- Submit Assignment
- Take Exam

---

# Why Use OOP?

Object-Oriented Programming provides several advantages:

- Organizes code into logical units.
- Makes code reusable.
- Reduces duplication.
- Simplifies maintenance.
- Makes large programs easier to understand.
- Models real-world objects naturally.

---

# Key Concepts of OOP

The four main concepts of Object-Oriented Programming are:

1. **Class**
2. **Object**
3. **Inheritance**
4. **Polymorphism**

You will learn each of these concepts in detail in the upcoming lessons.

---

# Summary

- OOP stands for **Object-Oriented Programming**.
- OOP organizes code using **objects**.
- Objects combine:
  - **Attributes (Data)**
  - **Methods (Actions)**
- OOP makes code more organized, reusable, and maintainable.
- It is widely used to model real-world entities in software development.


# Why Use Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is widely used because it helps developers write programs that are easier to organize, maintain, and reuse.

As software projects grow larger, OOP provides a structured way to manage code efficiently.

---

# Advantages of OOP

## 1. Organization

OOP organizes code into classes and objects.

This makes programs:

- Easier to read
- Easier to understand
- Easier to maintain

Large projects become much more manageable because related data and methods are grouped together.

---

## 2. Reusability

One of the biggest advantages of OOP is **code reuse**.

A class can be used to create multiple objects without rewriting the same code.

### Example

If you create a `Car` class, you can create many car objects:

- Toyota
- Honda
- Tesla

All of them use the same blueprint (class).

---

## 3. Easier Debugging

Since each object is self-contained, finding and fixing errors becomes easier.

Instead of searching through an entire program, you can focus on a specific class or object.

---

## 4. Real-World Modeling

OOP allows programmers to model real-world entities naturally.

For example:

| Real World | OOP |
|------------|-----|
| Student | Student Object |
| Car | Car Object |
| Bank Account | BankAccount Object |
| Mobile Phone | Phone Object |

Each object has:

- Attributes (data)
- Methods (actions)

---

# The Four Pillars of OOP

Object-Oriented Programming is based on four fundamental principles:

1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism

---

# 1. Abstraction

## Definition

**Abstraction** means hiding complex implementation details and showing only the essential features of an object.

Users interact with the object without needing to know how it works internally.

### Real-Life Example

Think of driving a car.

You use:

- Steering wheel
- Accelerator
- Brake pedal

You do **not** need to understand:

- Engine design
- Fuel injection system
- Internal mechanical components

The complex details are hidden from you.

This is abstraction.

---

# 2. Encapsulation

## Definition

**Encapsulation** is the process of combining data (attributes) and methods (functions) into a single unit (class) while controlling access to that data.

It helps protect data from accidental modification.

### Real-Life Example

A car's engine is enclosed inside the vehicle.

You cannot directly touch or modify its internal components while driving.

Instead, you interact with the car using:

- Steering wheel
- Accelerator
- Brake

The internal parts remain protected.

This is encapsulation.

---

# 3. Inheritance

## Definition

**Inheritance** allows one class to inherit the properties and methods of another class.

This promotes:

- Code reuse
- Reduced duplication
- Easier maintenance

### Real-Life Example

Suppose you already have a `Car` class.

A `SportsCar` class can inherit all the features of `Car`, such as:

- Wheels
- Engine
- Doors

Then it can add its own special features:

- Spoiler
- Turbo Engine
- Sport Mode

Instead of rewriting common code, the new class reuses the existing class.

---

# 4. Polymorphism

## Definition

**Polymorphism** means "many forms."

Different objects can respond to the same method in different ways.

The method name remains the same, but each object performs its own behavior.

### Real-Life Example

Suppose both a **Dog** and a **Cat** have a method called:

```python
make_sound()
```

When called:

- Dog → Barks
- Cat → Meows

Although the method name is the same, the behavior is different.

This is polymorphism.

---

# Summary Table

| Pillar | Meaning | Real-Life Example |
|---------|---------|-------------------|
| **Abstraction** | Hides implementation details and shows only essential features. | Driving a car without knowing how the engine works. |
| **Encapsulation** | Combines data and methods while protecting data. | A car's engine enclosed inside the vehicle. |
| **Inheritance** | One class acquires the properties and methods of another class. | A SportsCar inheriting features from a Car. |
| **Polymorphism** | Same method name, different behavior for different objects. | A Dog barks and a Cat meows using `make_sound()`. |

---

# Key Takeaways

- OOP makes code organized and easy to maintain.
- It promotes code reuse through classes.
- It simplifies debugging by organizing related code together.
- It models real-world objects naturally.
- OOP is built on four pillars:
  - Abstraction
  - Encapsulation
  - Inheritance
  - Polymorphism