// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from depthai_ros_msgs:srv/NormalizedImageCrop.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "depthai_ros_msgs/srv/detail/normalized_image_crop__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace depthai_ros_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _NormalizedImageCrop_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NormalizedImageCrop_Request_type_support_ids_t;

static const _NormalizedImageCrop_Request_type_support_ids_t _NormalizedImageCrop_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NormalizedImageCrop_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NormalizedImageCrop_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NormalizedImageCrop_Request_type_support_symbol_names_t _NormalizedImageCrop_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, depthai_ros_msgs, srv, NormalizedImageCrop_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, depthai_ros_msgs, srv, NormalizedImageCrop_Request)),
  }
};

typedef struct _NormalizedImageCrop_Request_type_support_data_t
{
  void * data[2];
} _NormalizedImageCrop_Request_type_support_data_t;

static _NormalizedImageCrop_Request_type_support_data_t _NormalizedImageCrop_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NormalizedImageCrop_Request_message_typesupport_map = {
  2,
  "depthai_ros_msgs",
  &_NormalizedImageCrop_Request_message_typesupport_ids.typesupport_identifier[0],
  &_NormalizedImageCrop_Request_message_typesupport_symbol_names.symbol_name[0],
  &_NormalizedImageCrop_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t NormalizedImageCrop_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NormalizedImageCrop_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace depthai_ros_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<depthai_ros_msgs::srv::NormalizedImageCrop_Request>()
{
  return &::depthai_ros_msgs::srv::rosidl_typesupport_cpp::NormalizedImageCrop_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, depthai_ros_msgs, srv, NormalizedImageCrop_Request)() {
  return get_message_type_support_handle<depthai_ros_msgs::srv::NormalizedImageCrop_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "depthai_ros_msgs/srv/detail/normalized_image_crop__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace depthai_ros_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _NormalizedImageCrop_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NormalizedImageCrop_Response_type_support_ids_t;

static const _NormalizedImageCrop_Response_type_support_ids_t _NormalizedImageCrop_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NormalizedImageCrop_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NormalizedImageCrop_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NormalizedImageCrop_Response_type_support_symbol_names_t _NormalizedImageCrop_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, depthai_ros_msgs, srv, NormalizedImageCrop_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, depthai_ros_msgs, srv, NormalizedImageCrop_Response)),
  }
};

typedef struct _NormalizedImageCrop_Response_type_support_data_t
{
  void * data[2];
} _NormalizedImageCrop_Response_type_support_data_t;

static _NormalizedImageCrop_Response_type_support_data_t _NormalizedImageCrop_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NormalizedImageCrop_Response_message_typesupport_map = {
  2,
  "depthai_ros_msgs",
  &_NormalizedImageCrop_Response_message_typesupport_ids.typesupport_identifier[0],
  &_NormalizedImageCrop_Response_message_typesupport_symbol_names.symbol_name[0],
  &_NormalizedImageCrop_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t NormalizedImageCrop_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NormalizedImageCrop_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace depthai_ros_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<depthai_ros_msgs::srv::NormalizedImageCrop_Response>()
{
  return &::depthai_ros_msgs::srv::rosidl_typesupport_cpp::NormalizedImageCrop_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, depthai_ros_msgs, srv, NormalizedImageCrop_Response)() {
  return get_message_type_support_handle<depthai_ros_msgs::srv::NormalizedImageCrop_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "depthai_ros_msgs/srv/detail/normalized_image_crop__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace depthai_ros_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _NormalizedImageCrop_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _NormalizedImageCrop_type_support_ids_t;

static const _NormalizedImageCrop_type_support_ids_t _NormalizedImageCrop_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _NormalizedImageCrop_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _NormalizedImageCrop_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _NormalizedImageCrop_type_support_symbol_names_t _NormalizedImageCrop_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, depthai_ros_msgs, srv, NormalizedImageCrop)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, depthai_ros_msgs, srv, NormalizedImageCrop)),
  }
};

typedef struct _NormalizedImageCrop_type_support_data_t
{
  void * data[2];
} _NormalizedImageCrop_type_support_data_t;

static _NormalizedImageCrop_type_support_data_t _NormalizedImageCrop_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _NormalizedImageCrop_service_typesupport_map = {
  2,
  "depthai_ros_msgs",
  &_NormalizedImageCrop_service_typesupport_ids.typesupport_identifier[0],
  &_NormalizedImageCrop_service_typesupport_symbol_names.symbol_name[0],
  &_NormalizedImageCrop_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t NormalizedImageCrop_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_NormalizedImageCrop_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace depthai_ros_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<depthai_ros_msgs::srv::NormalizedImageCrop>()
{
  return &::depthai_ros_msgs::srv::rosidl_typesupport_cpp::NormalizedImageCrop_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_cpp, depthai_ros_msgs, srv, NormalizedImageCrop)() {
  return ::rosidl_typesupport_cpp::get_service_type_support_handle<depthai_ros_msgs::srv::NormalizedImageCrop>();
}

#ifdef __cplusplus
}
#endif
