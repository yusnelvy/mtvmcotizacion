// funcion para el Event.observe
function register(element, eventName, handler) {
    var registry = getOrCreateRegistryFor(element);
    if (!registry[eventName]) registry[eventName] = [];
    var entries = registry[eventName];

    var i = entries.length;
    while (i--)
      if (entries[i].handler === handler) return null;

    var uid = getUniqueElementID(element);
    var responder = GLOBAL.Event._createResponder(uid, eventName, handler);
    var entry = {
      responder: responder,
      handler:   handler
    };

    entries.push(entry);
    return entry;
  }

function unregister(element, eventName, handler) {
    var registry = getOrCreateRegistryFor(element);
    var entries = registry[eventName] || [];

    var i = entries.length, entry;
    while (i--) {
      if (entries[i].handler === handler) {
        entry = entries[i];
        break;
      }
    }

    if (entry) {
      var index = entries.indexOf(entry);
      entries.splice(index, 1);
    }

    if (entries.length === 0) {
      delete registry[eventName];
      if (Object.keys(registry).length === 1 && ('element' in registry))
        destroyRegistryForElement(element);
    }

    return entry;
  }
 function observe(element, eventName, handler) {
    element = $(element);
    var entry = register(element, eventName, handler);

    if (entry === null) return element;

    var responder = entry.responder;
    if (isCustomEvent(eventName))
      observeCustomEvent(element, eventName, responder);
    else
      observeStandardEvent(element, eventName, responder);

    return element;
  }

  function observeStandardEvent(element, eventName, responder) {
    var actualEventName = getDOMEventName(eventName);
    if (element.addEventListener) {
      element.addEventListener(actualEventName, responder, false);
    } else {
      element.attachEvent('on' + actualEventName, responder);
    }
  }

  function observeCustomEvent(element, eventName, responder) {
    if (element.addEventListener) {
      element.addEventListener('dataavailable', responder, false);
    } else {
      element.attachEvent('ondataavailable', responder);
      element.attachEvent('onlosecapture',   responder);
    }
  }


