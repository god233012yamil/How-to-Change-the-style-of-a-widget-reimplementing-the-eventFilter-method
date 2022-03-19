# Introduction
This code shows how to change the stylesheet of a widget (QPushButton) when the mouse is pressed,
or the mouse is released, or the mouse enter into the widget, or the mouse leave from the widget.

Change the stylesheet of a widget, is a way for the application to respond to different actions while
the user is graphically notified. This technique enrich the graphic user interface experience.

For a widget to react to different events, an event filter must be installed on the widget and the method
eventFiler must be reimplemented. 

# What is an event filter?
An event filter is an object that receives all events that are sent to this object. The filter can either stop the event or forward it to this object. The event filter filterObj receives events via its eventFilter() function. The eventFilter() function must return true if the event should be filtered, (i.e. stopped); otherwise it must return false.

# The following are the steps to implement the eventFilter for three QPushButton.

# Step 1: Create instances of the Widgets to be watch.
self.button_1 = QPushButton()
self.button_2 = QPushButton()
self.button_3 = QPushButton()

# Step 1: Install an event filter on the objects to be watch.
self.button_1.installEventFilter(self)
self.button_2.installEventFilter(self)
self.button_3.installEventFilter(self)

# Step 3: Override the method eventFilter for the class MainWindow.
#         Check which object send the event and event type.
    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        # If a mouse press event has occurred.
        if event.type() == QtCore.QEvent.MouseButtonPress:
            # If the originator of the event is a QPushButton.
            if isinstance(source, QPushButton) and (source.objectName() == "Button 1" or
                                                    source.objectName() == "Button 3"):
                source.setStyleSheet(self.push_button_sunken_style)
                source.setText("Mouse pressed event")
                return True
        # If a mouse release event has occurred.
        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            # If the originator of the event is a QPushButton.
            if isinstance(source, QPushButton) and (source.objectName() == "Button 1" or
                                                    source.objectName() == "Button 3"):
                source.setStyleSheet(self.push_button_risen_style)
                source.setText("Mouse released event")
                return True
        #
        elif event.type() == QtCore.QEvent.Enter:
            # If the originator of the event is a QPushButton.
            if isinstance(source, QPushButton) and (source.objectName() == "Button 2" or
                                                    source.objectName() == "Button 3"):
                source.setStyleSheet(self.push_button_enter_style)
                source.setText("Mouse enter event")
                return True
        #
        elif event.type() == QtCore.QEvent.Leave:
            # If the originator of the event is a QPushButton.
            if isinstance(source, QPushButton) and (source.objectName() == "Button 2" or
                                                    source.objectName() == "Button 3"):
                source.setStyleSheet(self.push_button_leave_style)
                source.setText("Mouse leave event")
                return True
        else:
            return False
        return False
