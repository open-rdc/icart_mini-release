Name:           ros-indigo-icart-mini-gazebo
Version:        0.1.1
Release:        2%{?dist}
Summary:        ROS icart_mini_gazebo package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-gazebo-plugins
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-gazebo-ros-control
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-joint-limits-interface
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-transmission-interface
Requires:       ros-indigo-urdf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-gazebo-ros
BuildRequires:  ros-indigo-gazebo-ros-control
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-joint-limits-interface
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-transmission-interface
BuildRequires:  ros-indigo-urdf

%description
The icart_mini_gazebo package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Dec 17 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.1.1-2
- Autogenerated by Bloom

* Wed Dec 17 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.1.1-0
- Autogenerated by Bloom

* Wed Dec 17 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.1.1-1
- Autogenerated by Bloom

* Tue Dec 09 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.0.5-0
- Autogenerated by Bloom

* Tue Dec 02 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.0.3-1
- Autogenerated by Bloom

* Tue Dec 02 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.0.3-0
- Autogenerated by Bloom

